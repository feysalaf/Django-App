import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});


  constructor(private http: HttpClient) { }


  getallUsers(): Observable<any> {
    return this.http.get(this.baseurl + '/api/user/',
    {headers: this.httpHeaders});
  }

  createUser(user): Observable<any> {
    const body = {first_name: user.first_name , last_name: user.last_name, age: user.age, user_name:user.user_name };
    return this.http.post(this.baseurl + '/api/user/', body,
    {headers: this.httpHeaders});
  }
  createTweet(user): Observable<any> {
    const body = {tweet:user.tweet};
    return this.http.post(this.baseurl + '/api/tweet/',body,{headers:this.httpHeaders});
  }


}
