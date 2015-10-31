if [ $# -ne 1 ]
    then
        echo "Just throw in a short release message. I can figure out the tag."
    else
        description=$(git describe --abbrev=0)
        tag=$(($description + 1))
        git tag -a $tag -m "$1"
        git push origin HEAD --follow-tags
    # git push origin --set-upstream HEAD
    #   A handy way to push the current branch to the same name on the
    #   remote.
    # --follow-tags
    #   Also push annotated tags in refs/tags that are missing from the
    #   remote but are pointing at commit-ish that are reachable from the
    #   refs being pushed
fi
