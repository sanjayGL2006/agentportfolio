"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { Download, TrendingUp, CheckCircle, AlertTriangle, XCircle } from "lucide-react";

export default function DashboardOverview() {
  const score = 78;

  const metrics = [
    { name: "Name Consistency", score: 85, status: "good" },
    { name: "Username Consistency", score: 65, status: "warning" },
    { name: "Profile Completeness", score: 90, status: "good" },
    { name: "Search Visibility", score: 72, status: "warning" },
    { name: "Website SEO", score: 88, status: "good" },
    { name: "Social/Profile Authority", score: 75, status: "warning" },
    { name: "Entity/Brand Consistency", score: 60, status: "critical" },
  ];

  const getStatusColor = (status: string) => {
    switch (status) {
      case "good": return "text-green-500";
      case "warning": return "text-yellow-500";
      case "critical": return "text-red-500";
      default: return "text-primary";
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case "good": return <CheckCircle className="w-4 h-4 text-green-500" />;
      case "warning": return <AlertTriangle className="w-4 h-4 text-yellow-500" />;
      case "critical": return <XCircle className="w-4 h-4 text-red-500" />;
      default: return null;
    }
  };

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h2 className="text-3xl font-bold tracking-tight">Dashboard Overview</h2>
          <p className="text-muted-foreground mt-1">
            Analyzing digital presence for <span className="text-primary font-medium">Sanjay G L</span>
          </p>
        </div>
        <button className="inline-flex items-center space-x-2 bg-primary text-primary-foreground px-4 py-2 rounded-lg font-medium shadow-lg shadow-primary/25 hover:bg-primary/90 transition-colors">
          <Download className="w-4 h-4" />
          <span>Generate SEO Report</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="md:col-span-1 bg-gradient-to-br from-card to-card/50 border-primary/20">
          <CardHeader>
            <CardTitle>Overall SEO Score</CardTitle>
            <CardDescription>Your personal brand search visibility</CardDescription>
          </CardHeader>
          <CardContent className="flex flex-col items-center justify-center py-6">
            <div className="relative flex items-center justify-center w-40 h-40">
              <svg className="w-full h-full transform -rotate-90">
                <circle cx="80" cy="80" r="70" className="text-muted stroke-current" strokeWidth="12" fill="transparent" />
                <circle 
                  cx="80" cy="80" r="70" 
                  className="text-primary stroke-current transition-all duration-1000 ease-out" 
                  strokeWidth="12" 
                  strokeDasharray="440" 
                  strokeDashoffset={440 - (440 * score) / 100}
                  strokeLinecap="round" 
                  fill="transparent" 
                />
              </svg>
              <div className="absolute flex flex-col items-center">
                <span className="text-5xl font-bold">{score}</span>
                <span className="text-sm text-muted-foreground">/ 100</span>
              </div>
            </div>
            <div className="mt-6 flex items-center space-x-2 text-sm text-yellow-500 font-medium">
              <AlertTriangle className="w-4 h-4" />
              <span>Needs Improvement</span>
            </div>
          </CardContent>
        </Card>

        <Card className="md:col-span-2">
          <CardHeader>
            <CardTitle>Detailed Metrics</CardTitle>
            <CardDescription>Breakdown of your digital identity score</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-5">
              {metrics.map((metric) => (
                <div key={metric.name} className="space-y-2">
                  <div className="flex justify-between items-center text-sm">
                    <div className="flex items-center space-x-2">
                      {getStatusIcon(metric.status)}
                      <span className="font-medium">{metric.name}</span>
                    </div>
                    <span className="font-bold">{metric.score}/100</span>
                  </div>
                  <Progress 
                    value={metric.score} 
                    className="h-2" 
                    indicatorClassName={
                      metric.status === 'good' ? 'bg-green-500' :
                      metric.status === 'warning' ? 'bg-yellow-500' : 'bg-red-500'
                    }
                  />
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Top Keyword</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">"Sanjay G L developer"</div>
            <p className="text-xs text-muted-foreground mt-1 flex items-center">
              <TrendingUp className="w-3 h-3 mr-1 text-green-500" /> +12% this month
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Identities Found</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">4 variations</div>
            <div className="flex gap-2 mt-2">
              <Badge variant="outline">Sanjay G L</Badge>
              <Badge variant="outline">sanjaygl30ai</Badge>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Critical Issues</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-red-500">3</div>
            <p className="text-xs text-muted-foreground mt-1">Requires immediate attention</p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
