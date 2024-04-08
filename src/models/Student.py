# class for retrieving student info from supabase
import supabase, datetime, pytz
from supabase import create_client,Client

class Student():
    API_URL= "https://hphnqflbwqmfdvsfqkqi.supabase.co"
    API_KEY= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaG5xZmxid3FtZmR2c2Zxa3FpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE1MjkwNjcsImV4cCI6MjAyNzEwNTA2N30.TA6JQ3L8ML7yv4f2Tst4dJ8MsokYmcc5JLKU2-iumiI"
        
    sr_code=""
    first_name=""
    last_name=""
    program=""
    
    def fetchStudentInfo(self, sr_code):
        supabase = create_client(self.API_URL, self.API_KEY)
        student_info = supabase.table("Student").select("*").eq("sr_code", sr_code).execute()
        return student_info.data[0]
        
    def insertStudentHistory(sr_code): # still on work
        time_in= datetime.now(pytz.utc)
        time_out= datetime.now(pytz.utc)
        duration=(time_in-time_out).total_seconds()
        
        student_info = supabase.table("History").insert({
            "sr_code": sr_code,
            "time_in": time_in,
            "time_out": time_out,
            "duration": duration
            
        }).execute()
        return student_info.data
        

