---
layout: post
title: Fixing Serialization exception in Jenkins pipeline
date: 2019-09-28 23:03:53
categories: pipeline groovy
---

I recently needed to parse a text file and convert it to a json file, all within a Jenkins pipeline. I ran into some interesting issues during that process that i'd like to share.

I had a file that looked like below, that I needed to group the apps by their environment

```text
dev/app1
dev/app2
stage/app3
prod/app4
...
```

Desired result

```json
{
  "dev": ["app1", "app2"],
  "stage": ["app3"],
  "prod": ["app4"]
}
```

I initially wrote some code that did the work.

```groovy
def envMap = [:].withDefault{key -> return []}
fileContents.eachLine { line ->
    split = line.split('/')
    def env = split[0]
    def app = split[1]
    envMap[env].add(app)
}
```

I ran it through Jenkins and I got an error: `java.io.NotSerializableException: groovy.lang.MapWithDefault`.
Not being too familiar with this error and groovy not being my strongest language, I did the next logical step, I Google'd the error.
We'll, I got a few hits but ultimately, it always ended up at the same location [JENKINS-38186](https://issues.jenkins-ci.org/browse/JENKINS-38186).

In short, using `MapWithDefault` cannot store the state of execution, so it can be paused/resumed (as i understand).

So, after a little trial and error, I change the logic to use a simpler approach, which worked!

```groovy
def envMap = [:]
fileContents.eachLine { line ->
    split = line.split('/')
    def env = split[0]
    def app = split[1]
    if (!envMap.containsKey(env)) {
        envMap.put(env, [])
    }
    envMap.get(env).add(app)
}
```
