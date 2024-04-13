from behave import *
import requests
import time


@given('API call')

def step_impl(context):

   context.url = "https://rickandmortyapi.com/"

@when('call "{endpoint}"')

def step_impl(context,endpoint):
   start_time = time.time()
   response = requests.get(context.url + endpoint)
   end_time = time.time()
   context.response_time = end_time - start_time
   context.response = response

@when('call API "/graphql"')

def step_impl(context):
   graphql_query = '''
    {
      characters {
        results {
          name
        }
      }
    }
    '''
   start_time = time.time()
   response = requests.post(context.url + "/graphql", json={"query": graphql_query})
   end_time = time.time()
   context.response_time = end_time - start_time
   context.response = response

@then('get status code {status_code}')

def step_impl(context,status_code):
   
   temp=status_code[len(status_code)-3:]
   assert context.response.status_code == int(temp), f"Expected status code: {temp}, received status code: {context.response.status_code}"



@then('response body get "{expected_text}"')

def step_impl(context,expected_text):

   assert expected_text in context.response.text, f"Expected text not found: {expected_text}"

@then('Call latecy is less than {max_latency}s')
def step_impl(context, max_latency):
    max_latency = float(max_latency)
    assert context.response_time < max_latency, f"High Latency: {context.response_time} secondi"
   