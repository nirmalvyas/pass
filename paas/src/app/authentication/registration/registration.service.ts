import { Injectable } from '@angular/core';
import { ApiRootService } from '../../shared/api-root.service';
import { HttpClient } from '../../../../node_modules/@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  constructor(private apiroot: ApiRootService, private http:HttpClient) { }

  postRegistration(data,callback){
    this.http.post(this.apiroot.registration(),data).subscribe((data)=>{
      callback(data);
    });
  }
}
