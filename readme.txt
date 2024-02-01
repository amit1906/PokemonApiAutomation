
- At test_3_top_5_fire_type_weight i assume there's no endpoint to retreive all pokemons of type 'fire' at once
  thus i make requests 'pokemon' to each one of the pokemon names i retreived by type 'fire',
  so i can get top 5 pokemons by ther'e weights.
  This amount of requests make the test last about 20 seconds.

- I added  assertions and strig helpers, to combine to assertion with the logging
  to avoid code duplications.

- The project has structure of: ExpectedFiles, Requests, Tests and Utils