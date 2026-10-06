"use client";

import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle2, Circle } from "lucide-react";

export default function ActionPlan() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Add Person Schema to website.", priority: "High", impact: "High", completed: true },
    { id: 2, text: "Add consistent 'Sanjay G L' identity across profiles.", priority: "High", impact: "High", completed: false },
    { id: 3, text: "Link LinkedIn → website.", priority: "Medium", impact: "High", completed: false },
    { id: 4, text: "Link GitHub → website.", priority: "Medium", impact: "High", completed: false },
    { id: 5, text: "Link website → LinkedIn.", priority: "High", impact: "Medium", completed: true },
    { id: 6, text: "Link website → GitHub.", priority: "High", impact: "Medium", completed: true },
    { id: 7, text: "Create an About page.", priority: "Low", impact: "Low", completed: false },
    { id: 8, text: "Create individual project pages (/projects/slug).", priority: "High", impact: "High", completed: true },
    { id: 9, text: "Create a consistent professional bio.", priority: "Medium", impact: "Medium", completed: false },
  ]);

  const toggleTask = (id: number) => {
    setTasks(tasks.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
  };

  const completedCount = tasks.filter(t => t.completed).length;

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Your SEO Action Plan</h2>
        <p className="text-muted-foreground mt-1">Step-by-step roadmap to solidify your digital presence.</p>
      </div>

      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Next 10 SEO Actions</CardTitle>
              <CardDescription>Progress: {completedCount} / {tasks.length} tasks completed</CardDescription>
            </div>
            <div className="text-2xl font-bold text-primary">
              {Math.round((completedCount / tasks.length) * 100)}%
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <div className="space-y-2">
            {tasks.map(task => (
              <div 
                key={task.id}
                className={`flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-lg border transition-all duration-200 cursor-pointer ${task.completed ? 'bg-muted/50 border-border opacity-70' : 'bg-card border-primary/20 hover:border-primary/50'}`}
                onClick={() => toggleTask(task.id)}
              >
                <div className="flex items-center space-x-3 mb-3 sm:mb-0">
                  <button className="shrink-0 text-muted-foreground hover:text-primary transition-colors">
                    {task.completed ? <CheckCircle2 className="w-6 h-6 text-green-500" /> : <Circle className="w-6 h-6" />}
                  </button>
                  <span className={`font-medium ${task.completed ? 'line-through text-muted-foreground' : 'text-foreground'}`}>
                    {task.text}
                  </span>
                </div>
                <div className="flex items-center space-x-2 sm:ml-4 pl-9 sm:pl-0">
                  <Badge variant={task.priority === 'High' ? 'destructive' : task.priority === 'Medium' ? 'warning' : 'secondary'}>
                    Priority: {task.priority}
                  </Badge>
                  <Badge variant={task.impact === 'High' ? 'success' : task.impact === 'Medium' ? 'warning' : 'outline'}>
                    Impact: {task.impact}
                  </Badge>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
