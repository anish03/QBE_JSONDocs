# QBE_JSONDocs
Implementation of Query by Example for JSON Documents

Supports ```insert, get and delete ``` operations.

## Input
```
add {"id":4,"last":"Smith","first":"James","location":{"city":"Seattle","state":"WA"},"active":false}
add {"id":1,"last":"Doe","first":"John","location":{"city":"Oakland","state":"CA"},"active":true}
add {"id":2,"last":"Stevens","first":"Jane","location":{"city":"San Francisco","state":"CA"},"active":true}
add {"id":3,"last":"Black","first":"Jack","location":{"city":"San Jose","state":"CA"},"active":true}
get {"location":{"state":"WA"},"active":true}
get {"id":1}
get {"active":true}
delete {"active":true}
get {}
```
