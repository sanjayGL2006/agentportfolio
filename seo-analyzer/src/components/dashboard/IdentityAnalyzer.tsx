"use client";

import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Search, UserCheck, AlertCircle, ArrowRight } from "lucide-react";

export default function IdentityAnalyzer() {
  const [primaryName, setPrimaryName] = useState("Sanjay G L");
  const [altNames, setAltNames] = useState("Sanjay GL\nSanjaygl\nSanjaygl2006\nSanjaygl200630\nSanju\nsanjaygl30ai");

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Name & Username Analyzer</h2>
        <p className="text-muted-foreground mt-1">Evaluate the consistency of your digital footprint.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Input Identities</CardTitle>
            <CardDescription>Enter the names and handles you use online.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <label className="text-sm font-medium">Primary Name</label>
              <input 
                type="text" 
                value={primaryName}
                onChange={(e) => setPrimaryName(e.target.value)}
                className="w-full bg-background border border-input rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium">Alternative Names & Usernames</label>
              <textarea 
                value={altNames}
                onChange={(e) => setAltNames(e.target.value)}
                rows={6}
                className="w-full bg-background border border-input rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary font-mono"
              />
            </div>
            <button className="w-full bg-primary/10 text-primary hover:bg-primary/20 py-2 rounded-md font-medium flex items-center justify-center transition-colors">
              <Search className="w-4 h-4 mr-2" /> Analyze Identities
            </button>
          </CardContent>
        </Card>

        <div className="space-y-6">
          <Card className="border-primary/50 bg-primary/5">
            <CardHeader className="pb-2">
              <CardTitle className="text-lg flex items-center">
                <UserCheck className="w-5 h-5 mr-2 text-primary" />
                Recommendations
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 pt-2">
              <div className="p-4 bg-background/50 rounded-lg border border-border">
                <p className="text-sm text-muted-foreground mb-1">Recommended primary identity:</p>
                <div className="text-xl font-bold text-foreground">Sanjay G L</div>
              </div>
              <div className="p-4 bg-background/50 rounded-lg border border-border">
                <p className="text-sm text-muted-foreground mb-1">Recommended universal username:</p>
                <div className="text-xl font-bold text-primary">sanjaygl30ai</div>
              </div>
              <p className="text-sm flex items-start space-x-2 text-muted-foreground">
                <ArrowRight className="w-4 h-4 mt-0.5 shrink-0 text-primary" />
                <span>Keep the exact spelling and spacing for <strong>Sanjay G L</strong> across LinkedIn, GitHub, and your personal website to build strong entity recognition.</span>
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Analysis Results</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-3">
                <li className="flex items-start space-x-3">
                  <AlertCircle className="w-5 h-5 text-yellow-500 shrink-0" />
                  <div className="text-sm">
                    <span className="font-semibold text-yellow-500 block">Brand Confusion Risk</span>
                    <span className="text-muted-foreground">"Sanjaygl200630" and "sanjaygl30ai" dilute your username consistency. Standardize to one.</span>
                  </div>
                </li>
                <li className="flex items-start space-x-3">
                  <UserCheck className="w-5 h-5 text-green-500 shrink-0" />
                  <div className="text-sm">
                    <span className="font-semibold text-green-500 block">Name Strength</span>
                    <span className="text-muted-foreground">"Sanjay G L" is distinct and indexable. Ensure the spaces are consistent (not "Sanjay GL").</span>
                  </div>
                </li>
              </ul>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
