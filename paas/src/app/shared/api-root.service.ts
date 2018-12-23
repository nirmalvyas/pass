import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiRootService {

  private IPADDRESS = "http://13.232.84.0";
  private users;
  private userregistration;

  constructor() {
    this.users = this.IPADDRESS+'/user',
    this.userregistration = this.IPADDRESS+'/users'
   }

   public user(){
     return this.users;
   }

   public registration(){
     return this.userregistration;
   }
}
