//
//  ViewController.swift
//  Temperature
//
//  Created by Shuo Ding on 1/25/15.
//  Copyright (c) 2015 Shuo Ding. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    

    @IBOutlet  var cLabel: UITextField!
    
    @IBOutlet  var fLabel: UILabel!
    
    
    @IBAction func getIt(sender: AnyObject) {
        var c = cLabel.text.toInt()
        if c != nil {
        var f = c! * 2
            f += 32
        fLabel.text = "Temp in F is: \(f) F"
        }
        else{
        fLabel.text="Please enter a number"
        
        }
    }
    
  
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

