# rt-ip

[![Build Status](https://travis-ci.org/raverat/rt-ip.svg?branch=master)](https://travis-ci.org/raverat/rt-ip)

# Requirements

* Python (2.7)
* Django (1.8)

# Installation

Add `'rt_ip.middleware.IPMiddleware'` to your `MIDDLEWARE_CLASSES` setting.

```python
  MIDDLEWARE_CLASSES = (
      ...
      'rt_ip.middleware.IPMiddleware',
      ...
  )
```

# Example

You can now retrieve the current ip into the `request` object.

```python
  def my_view(request):
      ip_address = request.ip_address
```

If you want to replace the `localhost` and `127.0.0.1` by an other ip address, you can do so by adding `RT_IP_LOCALHOST` setting.

```python
RT_IP_LOCALHOST = '192.168.0.1'
```

You can also substitutes other ip addresses with `RT_IP_SUBSTITUTES` setting.

```python
RT_IP_SUBSTITUTES = {
    '75.16.106.251': '91.95.170.89',
}
```

The `'75.16.106.251'` ip address will be replaced by `'91.95.170.89'`.
