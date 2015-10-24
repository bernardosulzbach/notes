if [ $# -ne 2 ]
    then
        echo "Pass two arguments: the new tag and a short release message."
    else
        git tag -a $1 -m "$2"
	git push origin HEAD --follow-tags
	# git push origin --set-upstream HEAD
	#   A handy way to push the current branch to the same name on the
	#   remote.
	# --follow-tags
	#   Also push annotated tags in refs/tags that are missing from the
	#   remote but are pointing at commit-ish that are reachable from the
	#   refs being pushed
fi
