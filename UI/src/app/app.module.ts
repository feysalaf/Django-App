import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegistrationComponent } from './registration/registration.component';
import { FeedComponent } from './feed/feed.component';
import { FollowingComponent } from './following/following.component';

@NgModule({
  declarations: [
    AppComponent,
    RegistrationComponent,
    FeedComponent,
    FollowingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
