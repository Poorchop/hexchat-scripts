use strict;

use HTTP::Async;
use HTTP::Request;
use JSON;
use XML::Simple;

Xchat::register("Video", "1.0");
Xchat::print("Video script loaded\n");

my $httpAsync = HTTP::Async->new();
my $jsonParser = JSON->new()->utf8();
my $xmlParser = XML::Simple->new(SuppressEmpty => '');
my @channels = ( '#sage', '#vodka-subs', '#commie-subs', '#arnavion' );
my @otherBots = ( 'Belfiore', 'Yotsugi' );

sub httpRequestAsync {
	my ($url, $callback) = @_;
	
	$httpAsync->add(new HTTP::Request(GET => $url));
	Xchat::hook_timer(50, sub {
		my $timer_result = Xchat::KEEP;
		my $response = $httpAsync->next_response;
		if ($response) {
			my $responseText = $response->decoded_content;
			if ($responseText) {
				$callback->($responseText, $response->decode);
			}
			$timer_result = Xchat::REMOVE;
		}
		return $timer_result;
	});
}

sub handler {
	my $channel = Xchat::get_info('channel');

	if (grep(/^$channel$/i, @channels) && !grep { Xchat::user_info($_) } @otherBots) {
		if (
			($_[0][1] =~ /(?:www\.)?youtube\.com\/watch\?(?:.*?&)?v=([^#& ?]*)/) ||
			($_[0][1] =~ /(?:www\.)?youtu\.be\/([^#& ?]*)/)
		) {
			httpRequestAsync('http://gdata.youtube.com/feeds/api/videos/' . $1 . '?v=2&alt=jsonc', sub {
				my $json = $jsonParser->decode($_[0]);
				if (exists $json->{data} && exists $json->{data}->{title}) {
					Xchat::command("msg $channel Youtube video title: $json->{data}->{title}");
				}
			});
		}
		
		elsif ($_[0][1] =~ /www\.nicovideo\.jp\/watch\/([^ ]+)/) {
			httpRequestAsync('http://ext.nicovideo.jp/api/getthumbinfo/' . $1 . '/title', sub {
				my $xml = $xmlParser->XMLin($_[1]);
				if (exists $xml->{thumb} && exists $xml->{thumb}->{title}) {
					Xchat::command("msg $channel Niconico video title: $xml->{thumb}->{title}");
				}
			});
		}
	}

	return Xchat::EAT_NONE;
}

Xchat::hook_print('Channel Action', \&handler);
Xchat::hook_print('Channel Message', \&handler);
Xchat::hook_print('Channel Msg Hilight', \&handler);
Xchat::hook_print('Your Action', \&handler);
Xchat::hook_print('Your Message', \&handler);
