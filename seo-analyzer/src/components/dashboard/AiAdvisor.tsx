"use client";

import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Sparkles, Copy, Check } from "lucide-react";

export default function AiAdvisor() {
  const [copied, setCopied] = React.useState<number | null>(null);

  const recommendations = [
    {
      title: "Recommended Website Title",
      content: "Sanjay G L (Sanju) – Full Stack AI Developer, Shivamogga"
    },
    {
      title: "Recommended Meta Description",
      content: "Sanjay G L (Sanju) – BCA student and Full Stack AI Developer in Shivamogga. 69 projects, 87 certificates, Python, React, AI."
    },
    {
      title: "Best LinkedIn Headline",
      content: "Full Stack AI Developer | Python | React | Shivamogga"
    },
    {
      title: "Best GitHub Bio",
      content: "Full Stack AI Developer | BCA Student @ PESIAMS. Building scalable web apps and AI integrations. #Python #React"
    }
  ];

  const handleCopy = (text: string, idx: number) => {
    navigator.clipboard.writeText(text);
    setCopied(idx);
    setTimeout(() => setCopied(null), 2000);
  };

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">AI SEO Advisor</h2>
        <p className="text-muted-foreground mt-1">AI-generated recommendations to optimize your profiles.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {recommendations.map((rec, idx) => (
          <Card key={idx} className="relative overflow-hidden group border-primary/20 bg-gradient-to-br from-card to-card/50">
            <div className="absolute top-0 right-0 w-32 h-32 bg-primary/5 rounded-full -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700" />
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground flex items-center space-x-2">
                <Sparkles className="w-4 h-4 text-primary" />
                <span>{rec.title}</span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex items-start justify-between">
                <p className="text-lg font-semibold pr-8 leading-snug">{rec.content}</p>
                <button 
                  onClick={() => handleCopy(rec.content, idx)}
                  className="shrink-0 p-2 bg-background border border-border rounded-md hover:bg-muted transition-colors z-10"
                >
                  {copied === idx ? <Check className="w-4 h-4 text-green-500" /> : <Copy className="w-4 h-4 text-muted-foreground" />}
                </button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
