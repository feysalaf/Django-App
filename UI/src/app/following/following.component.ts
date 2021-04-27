import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-following',
  templateUrl: './following.component.html',
  styleUrls: ['./following.component.scss']
})
export class FollowingComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }



  array = [
     {
         "id": 1,
         "first_name":"Michael",
         "last_name":"Smith",
         "user": "http://localhost:8000/api/user/1/",
         "tweet": "I got some pizza cravings"
     },
     {
         "id": 2,
         "first_name":"Drake",
         "last_name":"Smith",
         "user": "http://localhost:8000/api/user/1/",
         "tweet": "Replaced"
     },
     {
         "id": 3,
         "first_name":"John",
         "last_name":"Smith",
         "user": "http://localhost:8000/api/user/1/",
         "tweet": "I lost my keys again"
     }
 ]
   


}
