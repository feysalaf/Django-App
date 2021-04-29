import { Injectable,Injector } from '@angular/core';
import { ApiService } from './api.service';
import { HttpInterceptor } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor{

    constructor(private injector: Injector,private _apiService: ApiService){}

    intercept(req, next) {
      let authService = this.injector.get(ApiService)
      if(req.headers.get("skip")){
        //remove internal header
        return next.handle(req)
      }
      else{
        if(this._apiService.loggedIn()){
          let tokenizedReq = req.clone(
          {
          setHeaders: {
                  Authorization: `Token ${authService.getToken()}`
                }
            }
        )
          return next.handle(tokenizedReq)

      }
      return next.handle(req)
     }
     }

}
