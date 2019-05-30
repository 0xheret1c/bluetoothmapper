import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as $ from 'jquery';

@Component({
  selector: 'app-mac',
  templateUrl: './mac.component.html',
  styleUrls: ['./mac.component.css']
})
export class MacComponent implements OnInit {

  constructor(private http: HttpClient){
  }

  ngOnInit() {

    this.http.get('http://116.203.159.127:8080/Mitglieder/').subscribe(data => {

     //Namen von übermitteltert Datei in einem Array speichern
      var name = [];
      var count = 0;
      while (count < data[0].Name.length-1){
       name [count] = data[count].Name;
       count++;
      }
      
      $("#mac").click(function(){
      //Namen an den DOM binden
      var count2 = 0;

      while(count2 < name.length-1){
        $( "#platzhalter" ).append( '<p style="width: 100%; padding:8px;" id="beispiel">' + name[count2] + '</p>');
        count2++;
      }
      $("p").toggle();
      });

    });

  }
}
