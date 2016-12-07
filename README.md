# rwby
Python wrapper for Belarusian Railways ([rasp.rw.by](rasp.rw.by))


## Usage
```python
# date must be a datetime.date instance or ISO formatted string.
>>> rwby.search(from_station='Брэст', to_station='Мінск', date='2017-12-31', lang='be')
```
 


## Requirements 

Tested on python3.5