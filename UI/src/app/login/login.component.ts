import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  register;


  constructor(private api: ApiService,private _router:Router) { }

  ngOnInit(): void {
        this.register = {
          username: '',
          password:''
        }
    }
  loginUser(){
      this.api.loginUser(this.register).subscribe(
        response => {
          alert("User logged in!");
          localStorage.setItem('token', response.token);
          console.log("Token Stored");
          console.log("Token:" + localStorage.getItem('token'));
          this._router.navigate(['home']);

        },
        error => {
          console.log(error);
          alert("Error while logging in user");
        }
      )

  }

}
