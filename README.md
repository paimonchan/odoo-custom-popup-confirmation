# odoo-custom-popup-confirmation
Odoo custom popup confirmation. Should be called from backend code.

This module help you if you want to trigger show confirmation popup via python code.


## Usage

### python code
```python
def callback(self):
    # actual action after confirmation
    pass

def open_confirmation(self):
    """
    Example show confirmation popup before actual call function callback.
    """
    popup = self.env['paimon.popup.confirmation']
    message = 'Are you sure to this action?'
    action = popup.show(self, message, 'callback')
    return action
```

### xml
```xml
  <button 
      name="open_confirmation"
      type="object"
      string="Confirm ?"
      class="oe_highlight"/>
```

### More
For full example, you can visit [models/example.py](models/example.py)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
