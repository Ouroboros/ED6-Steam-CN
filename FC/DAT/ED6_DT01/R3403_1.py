import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3403_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3403_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(610490, -10, -60800, 0)
    OP_6C(225000, 0)
    OP_4A(0x0008, 255)
    ChrSetFlags(0x0008, 0x0010)
    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrSetPos(0x0101, 610110, -10, -60540, 180)
    ChrSetPos(0x0102, 609200, 0, -59580, 180)
    ChrSetPos(0x0107, 610360, 0, -59200, 180)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2090180720V哈啊～………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180721V……我真没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180722V#506F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180723V总、总觉得\n',
            '这里的气氛好像很沉重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090180724V嗯？啊啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180725V唉，没什么事啦。\n',
            '只是刚才被前辈痛骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180726V……你们找我有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180727V#006F啊，嗯。\n',
            '我们想麻烦您一点小事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180728V其实我们在寻找\n',
            '运输车用的小型导力引擎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180729V而它的保管场所\n',
            '似乎就在这附近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180730V您知道是放在哪儿的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180731V是运输车用的\n',
            '驱动导力器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180732V你们找那种东西\n',
            '要用来做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180733V#010F因为运输车在平原那里抛锚了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180734V是由于导力引擎的故障所引起的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090180735V啊，原来如此，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180736V就是说需要\n',
            '更换用的零件对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180737V这样我就可以放心交给你们了，\n',
            '请稍微等一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x00FE, 608790, -30, -62460, 3000, 0x00)
    ChrWalkTo(0x00FE, 609150, 10, -65420, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 608790, -30, -62460, 3000, 0x00)
    ChrWalkTo(0x00FE, 610200, -40, -62060, 3000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090180738V久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180739V因为库存已经所剩不多了，\n',
            '所以你们一定要送到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x00FE, 0x0000, 0x00000258, 0x000007D0, 0x00)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '驱动用导力器',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000007D0, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010160864V#000F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180741V#010F好，\n',
            '那么我们立刻回王先生那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180742V他们肯定还在托兰特平原那里。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180743V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090180744V你们也要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_069C')
    def lambda_069C():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_069C)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180745V#060F啊，好的。\n',
            '谢谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180746V#010F那我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0346, 1)
    OP_28(0x0029, 0x04, 0x08)
    OP_28(0x0029, 0x01, 0x0010)
    OP_28(0x0029, 0x01, 0x0020)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
