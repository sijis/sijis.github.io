---
layout: post
title: Filter collectd metrics
date: 2015-05-18 11:51:08
categories: collectd metrics
---
Recently I've needed to filter some of the metrics being shipped from collectd agents to our graphite instance.

The documentation on collectd to do this is very sparse, to say the least. Luckily someone in the #collectd channel and some trial and error on my part, I was able to get it working.

Here's is what an example filter:

{% highlight xml linenos %}
  LoadPlugin "match_regex"
  <Chain "PostCache">
    # only show system and user
    <Rule "ignore_cpu_metrics">
      <Match "regex">
        Plugin "^cpu"
        Type "^cpu$"
        TypeInstance "^(idle|interrupt|nice|softirq|steal|wait)$"
      </Match>
      Target "stop"
    </Rule>

    # only show read/write ops
    <Rule "ignore_disk_metrics">
      <Match "regex">
        Plugin "^disk"
        PluginInstance "^(dm|sd.*)"
        Type "^disk_(merged|octets|time)"
      </Match>
      Target "stop"
    </Rule>

    # Default target
    Target "write"
  </Chain>
{% endhighlight %}

The 'ignore_cpu_metrics' only gathers the 'system and user' metric and I'm only getting disk read/write operations in "ignore_disk_metrics".

All the magic in done using [Chains configs](https://collectd.org/wiki/index.php/Chains). You should also read up on the [naming schema](https://collectd.org/wiki/index.php/Identifier) to understand how the metrics sections are split up.

Enjoy!
