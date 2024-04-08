# Still on experiment, might use later

from supabase import create_client, Client

url = "https://hphnqflbwqmfdvsfqkqi.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaG5xZmxid3FtZmR2c2Zxa3FpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE1MjkwNjcsImV4cCI6MjAyNzEwNTA2N30.TA6JQ3L8ML7yv4f2Tst4dJ8MsokYmcc5JLKU2-iumiI"

supabase = create_client(url,key)
def test_func():
  resp = supabase.functions.invoke("hello-world", invoke_options={'body':{
      "name":"Marius"
    }
  })
  return resp

print(test_func())