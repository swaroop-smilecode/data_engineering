We need to do 2 activities as part of data cleaning.

#### <ins>Convert input data which is in json format to parquet format</ins>
Look at the data present inside the json file.
```python
{
 "kind": "youtube#videoCategoryListResponse",
 "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/S730Ilt-Fi-emsQJvJAAShlR6hM\"",
 "items": [
  {
   "kind": "youtube#videoCategory",
   "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/Xy1mB4_yLrHy_BmKmPBggty2mZQ\"",
   "id": "1",
   "snippet": {
    "channelId": "UCBR8-60-B28hp2BmDPdntcQ",
    "title": "Film & Animation",
    "assignable": true
   }
  },

data continues....
```

But, glue crawler expects both key & value in single line as below
![image](https://github.com/user-attachments/assets/541f958c-5920-47e7-9d38-9aada681dbf7)

So, convert the json data into parquet file format. Will use lambda service for this purpose.

#### <ins>We just need some of the input data</ins>
Input data has many keys & corresponding values. We just need one key named `items` & it's corresponding value.
