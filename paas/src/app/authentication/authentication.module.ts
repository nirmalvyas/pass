import { NgModule } from '@angular/core';
import { LoginComponent } from './login/login.component';
import { CommonModule } from '../../../node_modules/@angular/common';
import { SharedModule } from '../shared/shared.module';
import { RegistrationComponent } from './registration/registration.component';


@NgModule({
  declarations: [
    LoginComponent,
    RegistrationComponent
  ],
  imports: [
    CommonModule,
    SharedModule
  ],
  providers: []
})
export class AuthenticationModule { }
