import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-panel',
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.scss']
})
export class PanelComponent implements OnInit {
  selectedUser;
  array = [];

  constructor(private api: ApiService) {
  this.selectedUser = { };
  }

  ngOnInit(): void {
  }

  createTweet = () => {
    this.api.createTweet(this.selectedUser).subscribe(
      data => {
        this.array.push(data);
      },
      error => {
        console.log(error);
      }
    );    }

}
