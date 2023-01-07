# Token auth in odoo controllers
Allow users to auth through http header token.

## Usage

1. Generate token in `res.users` form view
2. Use `auth=token` in controllers

```python
from odoo import http

class TestController(http.Controller):
    @http.route('/test', auth='token', csrf=False)
    def index(self, **kw):
        return "Hello, world"
```
