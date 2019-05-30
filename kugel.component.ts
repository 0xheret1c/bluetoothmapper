import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-kugel',
  templateUrl: './kugel.component.html',
  styleUrls: ['./kugel.component.css']
})
export class KugelComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    $(document).ready(function(){
  
      //Demo-Kugel die sich auf der Karte bewegt
      var position = $('#kugel').position();
      var x = position.left;
      var y = position.top;
      var fertig = false;
  
      //Kugel geht nach rechts
      if (fertig=false || x==position.left){
      while( x < 600 ){
          x = x + 4;
          $('#kugel').animate({left: x + 'px'});
      }
      fertig=true;
      }
      // Kugel geht nach links
      if (fertig=true || y < position.top ){
      fertig=false;
      while ( y < 350 ){
          y = y + 4;
          $('#kugel').animate({top: y + 'px'});
      }
      fertig=true;
      }
    });
  }

}
