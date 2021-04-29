import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-following',
  templateUrl: './following.component.html',
  styleUrls: ['./following.component.scss'],
  providers: [ApiService]
})

export class FollowingComponent implements OnInit {
  array = [];

  constructor(private api: ApiService) {
      this.getUsers();
 }

  ngOnInit(): void {

  }

  getUsers=()=>{
    this.api.getallUsers().subscribe(
      msg =>{
        this.array = msg;
        console.log(msg);
        console.log("Following initialized...");
      },
      error=>{
        console.log(error);
      }
    )
  }


 //
 //  array = [
 //     {
 //         "id": 1,
 //         "first_name":"Michael",
 //         "last_name":"Smith",
 //         "user": "http://localhost:8000/api/user/1/",
 //         "tweet": "I got some pizza cravings"
 //     },
 //     {
 //         "id": 2,
 //         "first_name":"Drake",
 //         "last_name":"Smith",
 //         "user": "http://localhost:8000/api/user/1/",
 //         "tweet": "Replaced"
 //     },
 //     {
 //         "id": 3,
 //         "first_name":"John",
 //         "last_name":"Smith",
 //         "user": "http://localhost:8000/api/user/1/",
 //         "tweet": "I lost my keys again"
 //     }
 // ]



}
