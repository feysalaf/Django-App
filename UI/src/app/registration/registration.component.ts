import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  //registation variables
  register;


  constructor(private api: ApiService,private _router:Router) { }

  ngOnInit(): void {
    this.register = {
      username: '',
      password:'',
      email:'',
    }
  }

  registerUser(){
      this.api.registerUser(this.register).subscribe(
        response => {
          alert("User Registered");
          console.log(response);
          localStorage.setItem('token', response.token);
          console.log("Token Stored");
          console.log("Token:" + localStorage.getItem('token'));
          this._router.navigate(['home']);

        },
        error => {
          console.log("Error while registering user");
        }
      )

  }

}
