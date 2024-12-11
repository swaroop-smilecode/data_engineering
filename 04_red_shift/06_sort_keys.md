#### What are sort keys?
- While you are creating table definition, if sort keys are specified, then while storing the data into table,</br>
  it will be stored in the respective sorted order mentioned by in sort keys list.</br>
- Defyining sort keys makes data retrieval fast, as there is no need of full table scan.</br>
![image](https://github.com/user-attachments/assets/b15dbf9b-ed4c-4c05-be5a-48e72aeb722f)


#### Types of sort keys
There are 2 types of sort keys.</br>
1. Compound sort keys
   This is the default sort key & we discussed above.
2. Interleaved sort keys
   I did not understood this.

#### Moral of the story about distribution key & sort key
Distribution key says into which slice, data has to be stored.</br>
Sort key says, in that slice, where should the data exactly go.
