import { Component} from '@angular/core';
import { TrainParams } from '../../models/trainParams';
import {FastApiService} from '../../services/fastapi.service';

@Component({
  selector: 'load-component',
  templateUrl: './load.component.html',
  styleUrls: ['./load.component.css']
})
export class LoadComponent {
  models: string[] = ['SVM', 'Decision Tree', 'Random Forest', 'Logistic Regression'];
  modelLoaded = false;
  trainParams = new TrainParams(this.models[0], './data/penguins_size.csv', 0.2);

  constructor(
    private _fastApiService: FastApiService,
  ) {
  }

  public onTrainClick(): void {
    console.log(this.trainParams);
    this._fastApiService.load(this.trainParams).subscribe(
      _ => this.modelLoaded = true
    );
  }
}
