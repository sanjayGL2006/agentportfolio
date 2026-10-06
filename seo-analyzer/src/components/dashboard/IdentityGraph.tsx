"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Network } from "lucide-react";

export default function IdentityGraph() {
  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Digital Identity Graph</h2>
        <p className="text-muted-foreground mt-1">Visualize how search engines connect your different profiles.</p>
      </div>

      <Card className="min-h-[500px] flex flex-col">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Network className="w-5 h-5 text-primary" />
            <span>Entity Connections</span>
          </CardTitle>
          <CardDescription>
            A strong identity graph helps search engines understand that these profiles represent the same person.
          </CardDescription>
        </CardHeader>
        <CardContent className="flex-1 flex items-center justify-center relative p-8">
          <div className="relative w-full max-w-2xl aspect-video rounded-xl border border-border/50 bg-background/50 overflow-hidden flex items-center justify-center">
            
            {/* Simple CSS-based Graph Visualization */}
            <div className="absolute inset-0 flex items-center justify-center opacity-20 pointer-events-none">
              <svg className="w-full h-full">
                <line x1="50%" y1="20%" x2="50%" y2="50%" stroke="currentColor" strokeWidth="2" strokeDasharray="4" />
                <line x1="50%" y1="50%" x2="20%" y2="80%" stroke="currentColor" strokeWidth="2" />
                <line x1="50%" y1="50%" x2="50%" y2="80%" stroke="currentColor" strokeWidth="2" />
                <line x1="50%" y1="50%" x2="80%" y2="80%" stroke="currentColor" strokeWidth="2" />
                <line x1="20%" y1="80%" x2="50%" y2="80%" stroke="currentColor" strokeWidth="2" strokeDasharray="4" />
                <line x1="50%" y1="80%" x2="80%" y2="80%" stroke="currentColor" strokeWidth="2" strokeDasharray="4" />
              </svg>
            </div>

            <div className="flex flex-col items-center z-10 w-full h-full justify-between py-12 relative">
              <div className="px-6 py-3 bg-primary text-primary-foreground rounded-full shadow-lg shadow-primary/20 font-bold text-lg animate-pulse duration-3000">
                Sanjay G L
              </div>
              
              <div className="px-5 py-2 bg-secondary text-secondary-foreground rounded-full shadow-md font-medium text-sm border border-border">
                sanjaygl30ai
              </div>

              <div className="flex w-full justify-around px-12">
                <div className="px-4 py-2 bg-card border border-border rounded-lg shadow-sm text-sm font-medium flex flex-col items-center">
                  <span className="text-blue-500 mb-1">LinkedIn</span>
                  <span className="text-xs text-muted-foreground">sanjay-gl-b86631336</span>
                </div>
                <div className="px-4 py-2 bg-card border border-primary/50 rounded-lg shadow-md shadow-primary/10 text-sm font-bold flex flex-col items-center scale-110">
                  <span className="text-primary mb-1">Personal Website</span>
                  <span className="text-xs text-muted-foreground">sanjaygl30ai.vercel.app</span>
                </div>
                <div className="px-4 py-2 bg-card border border-border rounded-lg shadow-sm text-sm font-medium flex flex-col items-center">
                  <span className="text-foreground mb-1">GitHub</span>
                  <span className="text-xs text-muted-foreground">sanjayGL2006</span>
                </div>
              </div>
            </div>
            
            <div className="absolute bottom-4 left-4 text-xs text-muted-foreground bg-background/80 px-2 py-1 rounded backdrop-blur-sm border border-border">
              Dashed lines indicate weak connections. Solid lines are verified links.
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
