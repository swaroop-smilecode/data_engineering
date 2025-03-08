To simulate this example, we have created a simple (local) API that allows us to retrieve user events.</br>
For example, we can retrieve the full list of available events from the past 30 days using the following API call:
```python
curl -o /tmp/events.json http://localhost:5000/events
```
