import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '../../../../node_modules/@angular/forms';
import { RegistrationService } from './registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {

  regForm: FormGroup;
  resetForm = true;
  submitted = true;
  message;

  constructor(private service: RegistrationService) { }

  ngOnInit() {
    this.regForm = new FormGroup({
      'first_name': new FormControl(null,Validators.required),
      'last_name': new FormControl(null,Validators.required),
      'email': new FormControl(null,[Validators.required,Validators.email]),
      'pan_number': new FormControl(null,Validators.required),
      'mobile': new FormControl(null,Validators.required),
      'dob': new FormControl(null,Validators.required)
    });
  }


  onSubmit(){
    console.log(this.regForm);
    if(this.regForm.valid){
      this.submitted = true;
      let dd = this.regForm.value.dob.getDate();
      let mm = this.regForm.value.dob.getMonth() + 1;
      let yyyy = this.regForm.value.dob.getFullYear();
      // console.log(yyyy + "-" + mm + "-" + dd);
      const date = yyyy+'-'+mm+'-'+dd;
      let input = new FormData();
      input.append('first_name', this.regForm.value.first_name);
      input.append('last_name', this.regForm.value.last_name);
      input.append('email', this.regForm.value.email);
      input.append('pan_number', this.regForm.value.pan_number);
      input.append('mobile', this.regForm.value.mobile);
      input.append('dob', date);
      this.service.postRegistration(input,(response)=>{
        console.log(response);
        this.message = response.message;
        setTimeout(()=>{
          this.message = '';
        },2000);
      });

      this.regForm.reset();
      this.resetForm = false;
      setTimeout(()=>{
        this.resetForm = true;
      },500);
    } else {
      this.submitted = false;
    }
  }
}
