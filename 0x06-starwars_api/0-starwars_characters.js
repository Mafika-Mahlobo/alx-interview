#!/usr/bin/node

const request = require("request");

if (process.argv.length === 3) {
   
   const movieId = parseInt(process.argv[2])
   const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

   request(url, (error, res, body) => {
      if (error) {
         console.error("Error:", error);
      } else {
         const data = JSON.parse(body);
	 const characters = data.characters
	 for (i = 0; i < characters.length; i++) {
            request(characters[i], (error, res, body) => {
               if (error) {
                 console.error("Error:", error);
	       } else {
		  const data = JSON.parse(body);
                  console.log(data.name);
	       }
	    });
	 }
     }
   });
} else {
   console.log("No arguments found!");
}
