import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl } from '../../../../node_modules/@angular/forms';
import { LoginserviceService } from './loginservice.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginform: FormGroup;
  resetForm = true;
  submitted = true;
  message;

  constructor(private service: LoginserviceService) { }

  ngOnInit() {
    this.loginform = new FormGroup({
      'user_name': new FormControl(null, Validators.required),
      'password': new FormControl(null,Validators.required)
    });
  }

  onSubmit(){
    console.log(this.loginform);
    if(this.loginform.valid){
      this.submitted = true;
      let input = new FormData();
      input.append('user_name', this.loginform.value.user_name);
      input.append('password', this.loginform.value.password);
      this.service.loginUser(input,(response)=>{
        console.log(response);
        this.message = response;
        setTimeout(()=>{
          this.message = '';
        },2000);
      });
      this.loginform.reset();
      this.resetForm = false;
      setTimeout(()=>{
        this.resetForm = true;
      },500);
    } else {
      this.submitted = false;
    }
  }

}
