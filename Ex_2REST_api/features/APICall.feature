Feature:Test API Rick & Morty

Scenario: /character call

Given  API call

When call "/api/character"

Then Call latecy is less than 1s

And response body get "results"

And get status code 200

Scenario: /graphql call

Given  API call

When call API "/graphql"

Then Call latecy is less than 1s

And response body get "characters"

And get status code 200

Scenario: negative test

Given  API call

When call "/api/appleseed"

Then Call latecy is less than 1s

And get status code not equal 200