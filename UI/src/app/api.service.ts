import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router'

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});


  constructor(private http: HttpClient,private _router:Router) { }


  getallUsers(): Observable<any> {
    return this.http.get(this.baseurl + '/api/profile/');
  }
  getTweets(): Observable<any> {
    return this.http.get(this.baseurl + '/api/tweet/');
  }
  getOneUser(id){
    return this.http.get(this.baseurl + '/api/profile/' + id + '/');
  }

  createUser(user): Observable<any> {
    const body = {first_name: user.first_name , last_name: user.last_name, age: user.age, user_name:user.user_name };
    return this.http.post(this.baseurl + '/api/profile/', body,
    {headers: this.httpHeaders});
  }
  createTweet(user): Observable<any> {
    const body = {tweet:user.tweet};
    return this.http.post(this.baseurl + '/api/tweet/',body,{headers:this.httpHeaders});
  }
  registerUser(userData): Observable<any> {
    return this.http.post(this.baseurl + '/api/register/',userData);
    this._router.navigate(['login']);
  }
  loginUser(userData): Observable<any> {
    return this.http.post(this.baseurl + '/api/login/',userData );
    this._router.navigate(['home']);
  }
  logoutUser(){
    //return this.http.post(this.baseurl + '/api/logout/');
    localStorage.removeItem('token');
  }
  // logoutUser() {
  //     localStorage.removeItem('token')
  //     this._router.navigate(['/events'])
  //   }

  getToken() {
    return localStorage.getItem('token')
  }
  loggedIn() {
    return !!localStorage.getItem('token')
  }


}
