import { Injectable } from '@angular/core';
import { ApiRootService } from '../../shared/api-root.service';
import { HttpClient } from '../../../../node_modules/@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginserviceService {

  constructor(private apiroot: ApiRootService, private http: HttpClient) { }

  loginUser(data,callback){
    this.http.post(this.apiroot.user()+'/login',data).subscribe((data)=>{
      callback(data);
    })
  }
}
