import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private _apiService: ApiService,
    private _router: Router) { }

  canActivate(): boolean {
    if (this._apiService.loggedIn()) {
      console.log('true')
      return true
    } else {
      console.log('false')
      this._router.navigate(['registration'])
      return false
    }
  }
}
