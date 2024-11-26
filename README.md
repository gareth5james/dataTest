# Prepare a JSON object from a csv file, ready for posting to an api.

Data is found in the "data.csv" file for our contacts in the following format

```
id  firstName   lastName    emailAddress ipAddress
```

We want to upload all of the contacts with a ".com" email address to our api.

# Your task

Using "index.js", read the "data.csv" file and output JSON into "output.json" in the following format;

```
{
    "items": [
        {
            "id": integer,
            "fullName": string, in the format "firstName lastName"
            "emailAddress": string,
            "ipAddress": string
        },
        {
            "id": integer,
            "fullName": string, in the format "firstName lastName"
            "emailAddress": string,
            "ipAddress": string
        },
        ... etc
    ]
}
```

