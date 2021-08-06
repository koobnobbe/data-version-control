import { LoadComponent } from '../components/load/load.component';
import { PredictComponent } from '../components/predict/predict.component';
import { Routes } from '@angular/router';

export const routerConfig: Routes = [
    {
        path: 'load',
        component: LoadComponent
    },
    {
        path: 'predict',
        component: PredictComponent
    },
    { path: '**', redirectTo: '/load', pathMatch: 'full' }
];
