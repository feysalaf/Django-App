import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  register;


  constructor(private api: ApiService) { }

  ngOnInit(): void {
        this.register = {
          first_name : '',
          last_name: '',
          user_name: '',
          age: '',
          password:''
        }
    }
  loginUser(){
      this.api.loginUser(this.register).subscribe(
        response => {
          console.log("User logged in ");
        },
        error => {
          console.log("Error while registering user");
        }
      )

  }

}
