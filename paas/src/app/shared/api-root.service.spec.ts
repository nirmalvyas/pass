import { TestBed } from '@angular/core/testing';

import { ApiRootService } from './api-root.service';

describe('ApiRootService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ApiRootService = TestBed.get(ApiRootService);
    expect(service).toBeTruthy();
  });
});
