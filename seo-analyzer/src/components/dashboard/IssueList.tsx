"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { AlertTriangle, XCircle, CheckCircle2, ArrowRight } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export default function IssueList() {
  const issues = [
    {
      type: "critical",
      title: "Primary name is not consistent across all profiles.",
      reason: "Search engines may index you as separate entities if names vary too much.",
      fix: "Standardize your display name to 'Sanjay G L' on GitHub, LinkedIn, and your website.",
    },
    {
      type: "critical",
      title: "Website is missing structured personal identity data.",
      reason: "Without Schema.org Person markup, Google has a harder time generating a Knowledge Panel for you.",
      fix: "Add JSON-LD Person schema to the <head> of your personal website.",
    },
    {
      type: "warning",
      title: "GitHub and LinkedIn identities should link back to the personal website.",
      reason: "Backlinks from authoritative social profiles pass SEO value to your personal site.",
      fix: "Ensure your website URL is explicitly listed in the website field of GitHub and LinkedIn.",
    },
    {
      type: "warning",
      title: "Some usernames use different naming patterns.",
      reason: "Using sanjayGL2006 and sanjaygl30ai dilutes brand recognition.",
      fix: "Where possible, migrate or alias to your primary handle 'sanjaygl30ai'.",
    },
    {
      type: "pass",
      title: "Personal website exists and is indexable.",
      reason: "Having a central hub is the most important step for personal SEO.",
      fix: "Keep publishing content and updating projects.",
    },
  ];

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">SEO Issues</h2>
        <p className="text-muted-foreground mt-1">Automatically detected issues holding back your digital presence.</p>
      </div>

      <div className="space-y-4">
        {issues.map((issue, idx) => {
          const isCritical = issue.type === "critical";
          const isWarning = issue.type === "warning";
          const isPass = issue.type === "pass";
          
          return (
            <Card key={idx} className={`border-l-4 ${isCritical ? 'border-l-red-500' : isWarning ? 'border-l-yellow-500' : 'border-l-green-500'}`}>
              <CardContent className="p-6">
                <div className="flex flex-col md:flex-row md:items-start gap-4">
                  <div className="shrink-0 mt-1">
                    {isCritical ? (
                      <XCircle className="w-6 h-6 text-red-500" />
                    ) : isWarning ? (
                      <AlertTriangle className="w-6 h-6 text-yellow-500" />
                    ) : (
                      <CheckCircle2 className="w-6 h-6 text-green-500" />
                    )}
                  </div>
                  <div className="flex-1 space-y-2">
                    <div className="flex items-center space-x-2">
                      <h3 className="font-semibold text-lg">{issue.title}</h3>
                      <Badge variant={isCritical ? "destructive" : isWarning ? "warning" : "success"}>
                        {isCritical ? "Critical" : isWarning ? "Warning" : "Passed"}
                      </Badge>
                    </div>
                    <p className="text-sm text-muted-foreground"><strong className="text-foreground">Why it matters:</strong> {issue.reason}</p>
                    
                    {!isPass && (
                      <div className="mt-4 p-4 bg-muted/50 rounded-lg border border-border flex items-start space-x-3">
                        <ArrowRight className="w-5 h-5 text-primary shrink-0 mt-0.5" />
                        <div>
                          <p className="text-sm font-medium">How to fix</p>
                          <p className="text-sm text-muted-foreground mt-1">{issue.fix}</p>
                          <button className="mt-3 text-xs bg-background border border-border px-3 py-1.5 rounded hover:bg-muted transition-colors font-medium">
                            Mark as Fixed
                          </button>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </div>
  );
}
