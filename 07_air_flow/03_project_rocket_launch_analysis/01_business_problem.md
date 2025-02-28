There is an API `https://ll.thespacedevs.com/2.0.0/launch/upcoming` which provides the details about upcoming rocket launches.</br>
Here is how the response looks like:</br>
```python
"results": [

{  
"id": "528b72ff-e47e-46a3-b7ad-23b2ffcec2f2",  
"url": "https://.../528b72ff-e47e-46a3-b7ad-23b2ffcec2f2/", "launch_library_id": 2103,  
"name": "Falcon 9 Block 5 | NROL-108",  
"net": "2020-12-19T14:00:00Z",  
"window_end": "2020-12-19T17:00:00Z",  
"window_start": "2020-12-19T14:00:00Z",  
➥ "image": "https://spacelaunchnow-prod- east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_image _20201217060406.jpeg",  
"infographic": ".../falcon2520925_infographic_20201217162942.png",  
...

}, {

"id": "57c418cc-97ae-4d8e-b806-bb0e0345217f",  
"url": "https://.../57c418cc-97ae-4d8e-b806-bb0e0345217f/", "launch_library_id": null,  
"name": "Long March 8 | XJY-7 & others",  
"net": "2020-12-22T04:29:00Z",  
"window_end": "2020-12-22T05:03:00Z",
"window_start": "2020-12-22T04:29:00Z",  
"image": "https://.../long2520march_image_20201216110501.jpeg", "infographic": null,  
...

},
... ]

}
```

This is what needs to be done:</br>
Hit the API --> Consume response & find image URL's --> Fetch those images.
