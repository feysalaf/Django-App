import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.scss'],
  providers: [ApiService]
})
export class FeedComponent implements OnInit {
  array = [];
  selectedUser;

  constructor(private api: ApiService) {
    this.getUsers();
    this.selectedUser = {id: -1, title: '' , desc: '', year: 0 };
  }

  getUsers = () => {
    this.api.getallUsers().subscribe(
      data => {
        this.array = data;
      },
      error => {
        console.log("Could not receive data...");
      }
    );
  }

   createUser = () => {
      this.api.createUser(this.selectedUser).subscribe(
        data => {
          this.array.push(data);
        },
        error => {
          console.log(error);
        }
      );
    }

  ngOnInit(): void {}


   //
   // array = [{
   //         first_name:"John",
   //         last_name:"Smith",
   //         age:0,},
   //         {
   //         first_name:"Michael",
   //         last_name:"Smith",
   //          age:0,},
   //        {first_name:"Drake",
   //          last_name:"Smith",
   //           age:0,}
   //
   //    ]


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
